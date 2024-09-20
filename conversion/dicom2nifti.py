import SimpleITK as sitk
import pydicom
import os
import ujson as json


def dcm2nifti(in_dir: str, out_dir: str) -> None:
    """
    Load dicom slices and store them in a volume
    :param in_dir: Directory where the dicom files are stored
    :param out_dir: Store path of the Nifti file
    :return: None
    """
    reader = sitk.ImageSeriesReader()
    dcm_series = reader.GetGDCMSeriesFileNames(in_dir)

    first_dicom_file = dcm_series[0]
    ds = pydicom.dcmread(first_dicom_file, stop_before_pixels=True)
    # series_uid = ds.SeriesInstanceUID
    meta = ds.to_json()

    reader.SetFileNames(dcm_series)
    image = reader.Execute()

    output_filename = os.environ.get('OUTPUT_FILE_NAME', 'UNNAMED_SERIES')

    patient_out = os.path.join(out_dir, f"{output_filename}.nii.gz")
    meta_out = os.path.join(out_dir, f"{output_filename}_meta.json")
    sitk.WriteImage(image, patient_out)

    with open(meta_out, 'w+') as meta_file:
        json.dump(meta, meta_file)


if __name__ == '__main__':
    out = os.path.join(os.path.sep, 'output')
    if not os.path.exists(out):
        os.makedirs(out, exist_ok=True)
    dcm2nifti(os.path.join(os.path.sep, 'data'), out)
