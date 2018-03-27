import os
import tesserocr
from PIL import Image as PIL_Image
from wand.image import Image as Wand_Image
import pickle

# If ImageMagick is not found, run export MAGICK_HOME=/usr/local/Cellar/imagemagick\@6/6.9.9-40/

TARGET_DIR = './grades-removed'

def extractTitles(target_dir):
  submissions_to_titles = {}
  for f in os.listdir(target_dir):
    infile = "{}/{}[0]".format(TARGET_DIR, f)
    pdf = Wand_Image(filename=infile, resolution = 300)
    pdf.crop(height=pdf.size[0]//3)
    pdf.save(filename = './temp.png')
    image = PIL_Image.open('./temp.png')
    ocr_text = tesserocr.image_to_text(image).strip()
    break_idx = ocr_text.find('\n\n')
    title = ocr_text[0:break_idx].replace('\n', ' ')
    submission_id = f.replace('.pdf', '')
    submissions_to_titles[submission_id] = title
    print("{} -> {}".format(submission_id, title))
    print(ocr_text)
    print("\n\n")
  with open('titles_dict.pkl', 'wb') as outfile:
    pickle.dump(submissions_to_titles, outfile)

def main():
  extractTitles(TARGET_DIR)

if __name__ == '__main__':
  main()