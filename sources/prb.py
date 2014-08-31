class matcher:
  #Phys rev B 
  # the 10.1103 comes from the doi
  fields = ['issue','papid']
  patterns = [
              "Phys[. ]+Rev[. ]+B[ ,]*(?P<issue>\d+)[, (]+(?P<year>\d+)[ ),]+(?P<papid>\d+)",
              "Phys[. ]+Rev[. ]+B[ ,]*(?P<issue>\d+)[, ]+(?P<papid>\d+)",
            ]
  journal_name = "Physical Review B"

  def urls(self):
    url =  "http://journals.aps.org/prb/abstract/10.1103/PhysRevB.{issue}.{papid}".format(issue=self.issue,papid=self.papid)
    return url
