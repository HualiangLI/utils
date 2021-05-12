# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
    # your path, remember to end with /
    path = "YOUR_PATH"
    for count, filename in enumerate(os.listdir(path)):
        surfix = os.path.splitext(filename)[-1]
        # the dist filename format
        dst = str(count).zfill(6) + surfix
        src = path + filename
        dst = path + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
