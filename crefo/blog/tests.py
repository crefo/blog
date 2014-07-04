from django.test import TestCase
# Create your tests here.
from models import Entries, Categories, TagModel
from broad import Broad

class broadTestCase(TestCase):

	def setUp(self):
		catem = Categories.objects.create(title='1')
		tagm = TagModel.objects.create(title='tag1')
		Entries.objects.create(title='test1', content='tttttttttttttttt1111', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test2', content='tttttttttttttttt1112', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test3', content='tttttttttttttttt1113', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test4', content='tttttttttttttttt1114', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test5', content='tttttttttttttttt1115', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test6', content='tttttttttttttttt1116', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test7', content='tttttttttttttttt1117', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test8', content='tttttttttttttttt1118', category=catem, pop = 0, readed=0)
		Entries.objects.create(title='test9', content='tttttttttttttttt1119', category=catem, pop = 0, readed=0)

	def test_broad_findByWord(self):
		"""check Word type"""

		broad = Broad()
		value = broad.findByWord('1',0)
		self.assertTrue( value, 'str' )
		value = broad.findByWord(1,0)
		self.assertTrue( value, 'int' )
		value = broad.findByWord(u'1',0)
		self.assertTrue( value, 'unicode' )


