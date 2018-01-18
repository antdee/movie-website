# Movie Trailer Website
This project contains a list of movies and series with their poster image, youtube trailer video and relevant details.
Then it creates an HTML code for a page to display all that information.

## Getting Started
To run this project as intended you would need to have all the following files in the same directory.
- `entertainment_center.py`  
This module will collect details for the movies and series
to be listed on the movie trailer website.
In the end it will call the function from the fresh_tomatoes.py module
create the `html` code and open it on the browser.  
To add a new entry simply create a new variable, call the `Movie` or `Serie` class and fill in the required description fields in the correct order, following the example of the entries already provided.  
You are encouraged to use url shorteners to stay within `pycodestyle` requirements.
Do not forget to add your new entry to the `movies` or `series` list at the end of the module.
- `fresh_tomatoes.py`  
This module will create the HTML for a simple website using information provided
from the module it is called from.  
Any changes and improvements to the output `html` code should be made here.
- `media.py`  
This module will store the parent / child Classes to be called in entertainment_center.py.  
Here we can add new information fields for our videos.
- `fresh_style.css`  
A short `stylesheet` for the added information not included in the original `fresh_tomatoes.py` module.  
Any style on further additions can be inserted here.


## Prerequisites

The project is meant to run on `Python 2.7` although it might be compatible with later versions of `Python`.
`Python 2.7.14` can be downloaded [here](https://www.python.org/downloads/).

## Deployment

To run the program, simply run the `entertainment_center.py` file.
You can do this from the `command line` by typing
 `$ python entertainment_center.py` from the directory all the files are located in.

The program will output an `html` file called `fresh_tomatoes.html` and immediately attempt to open it on your browser in a new tab.

The `html` page will first display all the movies listed, with their posters and youtube video link and after that will display all the series with their details.
Clicking on a movie / serie block will open the youtube trailer.

## Known Issues and Improvements Needed
- **Animation failure.**  
The `fresh_tomatoes.py` code originally had the capability to animate the positioning of movie blocks. Upon adding a second header, `List of Series` the animation stops and will not display further movie blocks, particularly the series ones.
For this reason the animation code part is commented out, `lines` `89` to `96` in `fresh_tomatoes.py`.
- **Scaling issue for multiple series.**  
With the current code setup, if we add more series or even just seasons they will simpy continue to be displayed as a list after the 12th episode on Ray Donovan.  
Display needs to be improved for that.
- **Long descriptions missalign blocks.**  
If a description of a movie or serie is long enough to make its block taller than the rest ones on the same row, it will cause a misaligning issue on the following row, leaving what would seem like blank blocks.   
To recreate this, one can simply go to the `avatar` entry on the `entertainment_center.py` and add a couple of lines of text to the title, description, date  or rating.
- **Repeating code.**  
There is some similar code that is being used twice over in the `fresh_tomatoes.py` module.  
Check `lines` `138` to `158`, and `lines` `165` to `205`.
- `fresh_style.css`.  
The styles contained in this file would surely fit with the rest called on the above lines `25 - 26` of the `fresh_tomatoes.py` module, however I do not know how to edit those.
