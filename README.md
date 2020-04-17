![](https://github.com/ubuntu-Deutschland-eV/ubucon.de/workflows/Build%20HTML%20of%20site/badge.svg?branch=master)

# File Structure – Where should i put my content?

Each year has own subfolders inside `content` *and* `content/pages`,
for example `content/2011` and `content/pages/2011`.

 * (news-)articles get inside of f.e. `content/2011`
 * pages get inside of f.e. `content/pages/2011`. In comparison to
 articles, pages dont change often and readers are not notified via RSS
 about changes. Pages can be used for example for informations about
 the event-location or the contact-page.
 * static-files like images, zip-archives get into `content/files`. You can link
 from articles to them via `[great description]({filename}/files/<myfile>)`

So, to start into a new year, just run `mkdir content/2222
content/pages/2222`. To define which entries are in the menu, just edit
`MENUITEMS` inside of `pelicanconf.py`. Older pages will be accessible
via the archive.

For further informations see
<http://docs.getpelican.com/en/stable/content.html>

# Local Development

Clone the git-Repository via

    $ git clone git@github.com:ubuntu-Deutschland-eV/ubucon.de.git

Furthermore, install virtualenv for Python 3. If you use Ubuntu via

    $ sudo apt install python3-virtualenv

To install all dependencies, run

    $ make install

To test locally, you can run

    $ make devserver

You can visit the site in your browser at `http://127.0.0.1:8000`. If you change
something of the content or the theme, the site should be rebuild in the background
automatically. Otherwise you can run the above command a second time to
restart the development server. To stop the development server run

    $ make stopserver

# Deployment

Build the HTML from the Markdown-files lying in `content`

    $ make publish

Everything in `output` can be put to the webserver.

After every push to github, github actions will automatically build a new
ZIP-archive with the contents of the output directory. The archive can be
found at <https://github.com/ubuntu-Deutschland-eV/ubucon.de/actions?query=workflow%3A%22Build+HTML+of+site%22>.

# Theme

**You only have to build the CSS if you made any changes.**

We use the „Ubuntu vanilla theme for Vanilla framework“ by Canonical Ltd.
See https://github.com/ubuntudesign/ubuntu-vanilla-theme
It's licensed under LGPLv3.

Furthermore, commit the changes directly into
https://github.com/ubuntu-Deutschland-eV/ubuntu-vanilla-theme and
update just the submodle-reference in this repository.

To build the CSS run

    npm install
    gulp build

inside `themes/verein/vendor/ubuntu-vanilla-theme`. If you don't want
to install ruby's gem system-wide, you have to install `ruby` and `scss-lint`
(latter via `gem install scss-lint`) manually. Moreover, you have to add the
location of the gem-binaries to the `PATH` manually, f.e.:

    PATH=$HOME/.gem/ruby/2.3.0/bin:$PATH gulp build
