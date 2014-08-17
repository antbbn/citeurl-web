CiteUrl
===========
This is a simple website whose aim is to help people find 
articles based on the references found in other literature.
It's hosted at [http://citeurl.herokuapp.com](http://citeurl.herokuapp.com/).

Details
==========
The web part is a very simple Flask app, the logic is all in app/views.py
and the frontend uses the templates/ html+Jinja files.
The engine if just a python module called 'sources', this is basically a collection
of regular expressions that allow one to match the typical citation format found
in a paper References section.
Using the matched content one then should be able to build an URL pointig to the publisher
web page for said article.

Contributing
============
You can contribute in a lot of ways, since there are many areas that require improvement.

Expanding the journal list
--------------------------
This is one of the most important thing at the moment and you can help by
* Suggesting a new journal by providing some example citation and urls to the corresponding articles
* If you like writing python code or regexp i will happly include your extension to the 'soruces' module,
    you can use the ones already present as an example (eg sources/mnras.py or sources/prd.py).

Website improvement, bugs
--------------------------
Given that I am not the best web developer i will appreciate any suggestions or help to improve the
overall experience so please feel free to drop me a line.


Antonio Bibiano
