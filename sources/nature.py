class matcher:
  # Nature OpenURL
    #http://www.nature.com/openurl/?genre=article&title=&volume=438&spage=197&issue=7065
  fields = ['volume','spage']
  patterns = [
              "Nature[ ,]+(?P<volume>\d+)[, ]+(?P<spage>\d+)",
              "Nature[ ,]+(?P<volume>\d+)\.(?P<issue>\d+)[ ,]+\((?P<year>\d+)\)[ :,]+(?P<spage>\d+)",
            ]
  journal_name = "Nature (OpenURL)"

  def urls(self):
    url = "http://www.nature.com/openurl/?genre=article&title=Nature&volume={volume}&spage={spage}".format(volume=self.volume,spage=self.spage)
    return url
