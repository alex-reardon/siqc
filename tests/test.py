
import siqc


def main() :
    local_data_path = 'src/'
    input_bucket = "loni-data-curated-20230501"
    input_prefix = 'ppmi_500_updated_cohort/curated/data/PPMI/137482/20220411/T1w/1575181/'
    output_bucket = 'tempamr' # FIXME
    output_prefix = 'output_prefix/'  # FIXME


    ## Get filepaths
    keys = siqc.search_s3(input_bucket, input_prefix, '.nii.gz')
    for key in keys :
        file_path = siqc.get_object(input_bucket, key, local_data_path)

    ## Read in image
    img = siqc.read_img(file_path)
    
    
    ## Image Processing (EXAMPLES)
    out_imgs, out_names = siqc.choose_function(img, 'remove_slices', file_path, output_bucket, output_prefix)
    #out_imgs, out_names = siqc.choose_function(img, 'resize_vox', file_path, output_bucket, output_prefix)
    #out_imgs, out_names = siqc.choose_function(img, 'rotate_img', file_path, output_bucket, output_prefix)
    #out_imgs, out_names = sqic.choose_function(img, 'add_noise', file_path, output_bucket, output_prefix)
    
    out_imgs, out_names = siqc.choose_function(img, 'remove_slices', file_path, output_bucket, output_prefix)
    count = 0
    for img in out_imgs : 
        siqc.write_to_s3(file_path, img, output_bucket, output_prefix, out_names[count]) 
        count += 1



if __name__ == "__main__":
    main()
