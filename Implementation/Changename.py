import os 
  
# Function to rename multiple files 
def main(): 
    i = 1
      
    for filename in os.listdir("C:/Users/Trishok/Desktop/embedded/dataset/test/Victory_Gesture/"): 
        dst = str(i) + ".jpg"
        src = 'C:/Users/Trishok/Desktop/embedded/dataset/test/Victory_Gesture/'+ filename 
        dst = 'C:/Users/Trishok/Desktop/embedded/dataset/test/Victory_Gesture/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 