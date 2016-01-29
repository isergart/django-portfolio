# django-portfolio
A standalone app for artists, photographers, designers and so on. To display their works in the Internet-enabled social networks and opportunities review.
Implemented for Django Framework 1.9

## Technical task

Is my first app on Django Framework. Need to do the following:

- ~~Implementation in the form of a catalogue of works, divided by category.
The ability to sort and search~~
- Each work has its own gallery with the ability to insert video and(or) image and comment the work
- When downloading files, they are converted to the same size, are compressed and stored in a separate folder with the project title, the Name is taken via the slug field
- Display thumbnails in the Django admin
- Manual sorting of catalogue of works
- Ability to manually sort the galleries
- Display all categories in a shared directory in a separate gallery
- Displays the 10 latest works by categories on the main page
- All customers(partners) on the home page
- ~~A static page in Flatpages, with Markdown editor~~
- Used the tools of the artist in creating his work(system tags) on home page and sort by values
- Authorization for review via the social network Vkontakte, Facebook, Google, Twitter
- Ability to toggle display of works in the form of a list or slider
- Randomly changing image placeholder if the user has not uploaded any images
- Beautiful modern responsive design on Bootstrap

## Install in your project

Clone this repository from GitHub on your computer:

    $ git clone https://github.com/isergart/django-portfolio.git

Then register 'portfolio', in the 'INSTALLED_APPS' section of your project's settings:

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.comments',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.contenttypes',
        .......
        'portfolio',
    )
Add the following to your urls.py the following:

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        .......
        url(r'^', include('portfolio.urls')),
    ]

## Dependence
This application is dependent on the following batteries:

- flatpages
- pagedown
