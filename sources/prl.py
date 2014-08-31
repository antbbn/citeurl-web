class matcher:
  fields = ['issue','papid']
  patterns = [
              "Phys[. ]+Rev[. ]+Lett[. ,]*(?P<issue>\d+)[, ]+\((?P<year>\d+)\)[ ,]+(?P<papid>\d+)",
              "Phys[. ]+Rev[. ]+Lett[. ,]*(?P<issue>\d+)[, ]+(?P<papid>\d+)",
            ]
  journal_name = "Physical Review Letters"

  def urls(self):
    url =  "http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.{issue}.{papid}".format(issue=self.issue,papid=self.papid)
    return url
