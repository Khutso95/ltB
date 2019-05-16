import unittest
import find_exams as FE

#print(FE.getExams('examlist.csv'))
class FindExamsTest(unittest.TestCase):
	def test_getCourse(self):
		
		self.assertTupleEqual(FE.getCourse("Levitt/ELEN4010"),('Levitt', 'ELEN4010'))
	
	
	def test_getExams(self):
		"""comparing two dictionaries"""
		MyDict = {'ELEN4013': ('2020-06-01', 'SHWWB')}
		self.assertDictEqual(FE.getExams('examlist.csv'),MyDict)
	def test_getTimeTable(self):
		timeT = [('ELEN4013', [('2020-06-01', ('TBD', 'TBD')), ('SHWWB', ('TBD', 'TBD'))])]
		list2 = FE.getTimeTable({'ELEN4013': ('2020-06-01', 'SHWWB')},'examlist.csv')
		self.assertListEqual(list2,timeT)


if __name__ == "__main__":
	unittest.main()
