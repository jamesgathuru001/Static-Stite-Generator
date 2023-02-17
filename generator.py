import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Define the directories for the site content and templates
PAGE_DIR = 'pages'
TEMPLATE_DIR = 'templates'

# Define the file names for the site pages
HOME_PAGE = 'index.html'
ABOUT_PAGE = 'about.html'
ERROR_PAGE = '404.html'

# Load the Jinja2 templates
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
homepage_template = env.get_template('homepage.html')
article_template = env.get_template('article.html')
page_template = env.get_template('page.html')

# Initialize the list of articles
articles = []

# Loop through the Markdown files in the pages directory
for filename in os.listdir(PAGE_DIR):
    if filename.endswith('.md'):
        # Read the Markdown file and convert it to HTML
        with open(os.path.join(PAGE_DIR, filename)) as f:
            content = markdown.markdown(f.read())

        # Parse the title from the Markdown file
        title = content.split('\n')[0][1:].strip()

        # Determine the URL for the page
        if filename == 'index.md':
            url = HOME_PAGE
        else:
            url = filename[:-3] + '.html'

        # Create a dictionary for the article and add it to the list
        article = {'title': title, 'content': content, 'url': url}
        articles.append(article)

        # Generate the HTML for the article
        html = article_template.render(article=article)

        # Write the HTML to a file
        with open(os.path.join(os.getcwd(), url), 'w') as f:
            f.write(html)

# Generate the HTML for the homepage
homepage_html = homepage_template.render(articles=articles)

# Write the HTML to a file
with open(os.path.join(os.getcwd(), HOME_PAGE), 'w') as f:
    f.write(homepage_html)

# Generate the HTML for the about page
about_html = page_template.render(title='About', content='<p>This is the about page.</p>')

# Write the HTML to a file
with open(os.path.join(os.getcwd(), ABOUT_PAGE), 'w') as f:
    f.write(about_html)

# Generate the HTML for the 404 page
error_html = page_template.render(title='404 - Page Not Found', content='<p>The requested page was not found.</p>')

# Write the HTML to a file
with open(os.path.join(os.getcwd(), ERROR_PAGE), 'w') as f:
    f.write(error_html)
