import os
from PIL import Image, ImageFilter

def main():
    data_dir_path = u"./result/"  # save directory
    data_dir_path_in = u"./pra/"  # name of directory that you want to put effect
    file_list = os.listdir(r'./pra/') # name of directory that you want to put effect
    count=10

    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == u'.png' or u'.jpeg' or u'.jpg':
            img = Image.open(data_dir_path_in + '/' + file_name) 
            #tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
            #tmp.save(data_dir_path + '/' + root +'_r01.jpg')
            tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
            tmp.save(data_dir_path + '/' + root +'_r02.jpg') 
            #tmp = img.transpose(Image.ROTATE_90)
            #tmp.save(data_dir_path + '/' + root +'_r03.jpg')
            #tmp = img.transpose(Image.ROTATE_180)
            #tmp.save(data_dir_path + '/' + root +'_r04.jpg')
            #tmp = img.transpose(Image.ROTATE_270)
            #tmp.save(data_dir_path + '/' + root +'_r05.jpg')
            #tmp = img.filter(ImageFilter.FIND_EDGES)
            #tmp.save(data_dir_path + '/' + root +'_r06.jpg')
            tmp = img.filter(ImageFilter.EDGE_ENHANCE)
            tmp.save(data_dir_path + '/' + root +'_r07.jpg')
            tmp = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            tmp.save(data_dir_path + '/' + root +'_r08.jpg')
            tmp = img.filter(ImageFilter.UnsharpMask(radius=5, percent=150, threshold=2))
            tmp.save(data_dir_path + '/' + root +'_r09.jpg')
            tmp = img.filter(ImageFilter.UnsharpMask(radius=10, percent=200, threshold=5))
            tmp.save(data_dir_path + '/' + root +'_r10.jpg')

            
            for i in range(5, 365, 10):#rotate each 10 degree
                tmp = img.rotate(i)
                
                count += 1
                tmp.save(data_dir_path + '/' + root +'_r'+ str(count) +'.jpg')
            
            
if __name__ == '__main__':
    main()
