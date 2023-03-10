# Static-Stite-Generator

Welcome to the Static-Site Generator, the fun and easy way to turn your Markdown files into a fully-functional website!

Do you have a bunch of Markdown files lying around, filled with your brilliant ideas and insightful observations? Do you want to share your writing with the world, but don't want to mess around with complicated web development tools? Then the Static-Site Generator is the tool for you!

My generator takes a folder full of Markdown files and turns them into a complete website, complete with a homepage, articles, an about page, and even a custom 404 error page. With just a few simple steps, you can turn your writing into a beautiful website that's ready to share with the world.

This application was built by Python version 3.11.2.

#### 17th February 2023

#### By James Gathuru
#### Email: jamesgathuru001@gmail.com

### Description

This is a simple static-site generator in Python that uses Markdown and Jinja2 to generate a website from a folder of Markdown files. The generator assumes that you have a folder called pages that contains all of your Markdown files, and a folder called templates that contains your Jinja2 templates. It also generates a navigation bar with links to your homepage, articles, about page, and 404 page.

## User Stories

As a user of the application i should be able to:

* Once cloned, the user can run the script
* Use it on a folder full of Markdown files and turns them into a complete website.
* Generate a homepage, articles, an about page, and even a custom 404 error page..


## Setup/Installation Requirements

To install and run the project, follow these steps:

* Clone the repository: https://github.com/jamesgathuru001/Static-Stite-Generator.git.

* install Jinja2 

   ```$ pip install jinja2```

* Run the script using

   ```$ python generator.py.```


* The generated website will be located in the output directory.


## How to Use the Project

To use the project, you can follow these instructions:

* Create a directory containing your Markdown files.
* Modify the config.json file to include the relevant information about your website.
* Run the script using ```$ python generator.py.```.
* The generated website will be located in the output directory.


## Technologies Used

  * Python version 3.11.2
  * Jinja2
  * VS Code

## License

This project is licenced under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*

Copyright (c) 2023 James Gathuru