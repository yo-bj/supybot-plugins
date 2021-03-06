from supybot.test import *

class LCSHTestCase(PluginTestCase):
    plugins = ('LCSH',)

    def test_search(self):
        self.assertResponse('lcsh search Death Metal', 
            'Death metal (Music) <http://lcsh.info/sh2003006845>')

    def test_info(self):
      self.assertResponse('lcsh Remixes', 
          'Remixes ; see from: Club mixes, Dance mixes, Mixes (Music) ; ' +
          'broader: Electronic music <http://lcsh.info/sh85042350> ; ' +
          'related: Sound recordings--Remixing <http://lcsh.info/sh2001002661>, ' +
          'Underground dance music <http://lcsh.info/sh00000588>')

