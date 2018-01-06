# Movie Trailer Website
This website written in Python programming language and it  displays movies that has been named **The Best Movies of 2017** by New York Times newspaper. Webiste stores a list of the movies, including box art imagery and a movie trailer URL and it allows visitors to browse The Best Movies of 2017 movies , watch the trailers, see ratings of the movie and storyline of the movie. This project is  part of the Full Stack Web Developer Nanodeegree Programm at Udacity. 

## Getting Started
* To get started, fork this  [repository]("http://www.example.com/coolcereals") to GitHub 
* Clone the repo  `$git clone https://github.com/zkat/can.viewify.git`

## Prerequisites
Install object-oriented Python on Mac via Homebrew :
* Open up your terminal and enter the following command: ` /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`. You will be prompted several times during the installation process.

* Verify everything worked by typing the `brew help` command at the command line. Now, just type `brew install python` to get the latest version of Python 2. 
* Verify that Python installed correctly by simply typing `python` at the command line. You should be greeted by the Python Shell.

Install Python on Windows [Download Python Windows](https://www.python.org/downloads/) 
## Running the tests
After a succesfull installation of Python and downloading the project. Open the project in Python's IDE (IDLE) or in any IDE that work with Python. Run **media.py** file and it should render a web page with movies content.  The movie-website.py  module has a function called open_movies_page that takes in one argument, which is a list of movies, and creates an HTML file which will display all of your favorite movies.
```
def open_movies_page(movies):
  output_file = open('index.html', 'w')
 rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) 
  # open in a new tab, if possible
```
## Built with 
* [Bootstrap](http://bootstrapdocs.com/v3.0.3/docs/)  The Front-End Framework
* [Python](https://www.python.org/)  used to generate dynamic page

