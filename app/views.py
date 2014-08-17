import sources

from flask import render_template
from flask import request
from app import app

@app.route('/',methods=['GET', 'POST']) 
@app.route('/search',methods=['GET', 'POST'])
def search():
    url = None
    citation = None
    journal = None
    if request.method == 'POST':
        citation = request.form['citation']
        
        for source in sources.list:
          obj = source()
          if sources.match(obj,citation):
            url = obj.urls()
            journal = obj.journal_name
            break

    return render_template("search.html", url=url, journal=journal, citation=citation)


@app.route('/journals')
def journals():
    journals = []
    for source in sources.list:
        journals.append(source.journal_name)

    return render_template("journals.html", journals=journals)

@app.route('/about')
def about():
    return render_template("about.html")

