import unittest
import math
import triangle

class MyTest(unittest.TestCase):
	def test_type1(self):
		self.assertEqual(triangle.detect_triangle('a',2,3),"Nhap khong dung kieu")
	def test_type2(self):
		self.assertEqual(triangle.detect_triangle('a','ab',3),"Nhap khong dung kieu")
	def test_type3(self):
		self.assertEqual(triangle.detect_triangle(2,'a',3),"Nhap khong dung kieu")
	def test_type4(self):
		self.assertEqual(triangle.detect_triangle(2,3,'a'),"Nhap khong dung kieu")
	def test_type5(self):
		self.assertEqual(triangle.detect_triangle(3,'ab',2),"Nhap khong dung kieu")
	def test_type6(self):
		self.assertEqual(triangle.detect_triangle(3,2,'ab'),"Nhap khong dung kieu")
	def test_type7(self):
		self.assertEqual(triangle.detect_triangle('a','ab','abc'),"Nhap khong dung kieu")
	def test_type8(self):
		self.assertEqual(triangle.detect_triangle('a','abc','ab'),"Nhap khong dung kieu")
	def test_type9(self):
		self.assertEqual(triangle.detect_triangle('abc','a','ab'),"Nhap khong dung kieu")
	def test_input1(self):
		self.assertEqual(triangle.detect_triangle(-2,3,4),"So nhap vao khong dung")
	def test_input2(self):
		self.assertEqual(triangle.detect_triangle(3,-2,4),"So nhap vao khong dung")
	def test_input3(self):
		self.assertEqual(triangle.detect_triangle(3,4,-2),"So nhap vao khong dung")
	def test_input4(self):
		self.assertEqual(triangle.detect_triangle(-2,-3,4),"So nhap vao khong dung")
	def test_input5(self):
		self.assertEqual(triangle.detect_triangle(-3,-2,4),"So nhap vao khong dung")
	def test_input6(self):
		self.assertEqual(triangle.detect_triangle(-3,4,-2),"So nhap vao khong dung")
	def test_input7(self):
		self.assertEqual(triangle.detect_triangle(-2,-3,-4),"So nhap vao khong dung")
	def test_input8(self):
		self.assertEqual(triangle.detect_triangle(-3,-2,-4),"So nhap vao khong dung")
	def test_input9(self):
		self.assertEqual(triangle.detect_triangle(-3,-4,-2),"So nhap vao khong dung")
	def test_deu(self):
		self.assertEqual(triangle.detect_triangle(3,3,3),"Tam giac deu")
	def test_thuong1(self):
		self.assertEqual(triangle.detect_triangle(7,8,9),"Tam giac thuong")
	def test_thuong2(self):
		self.assertEqual(triangle.detect_triangle(8,7,9),"Tam giac thuong")
	def test_thuong3(self):
		self.assertEqual(triangle.detect_triangle(8,9,7),"Tam giac thuong")
	def test_can1(self):
		self.assertEqual(triangle.detect_triangle(7,9,7),"Tam giac can")
	def test_can2(self):
		self.assertEqual(triangle.detect_triangle(7,7,9),"Tam giac can")
	def test_can3(self):
		self.assertEqual(triangle.detect_triangle(9,7,7),"Tam giac can")
	def test_vuong1(self):
		self.assertEqual(triangle.detect_triangle(3,4,5),"Tam giac vuong")
	def test_vuong2(self):
		self.assertEqual(triangle.detect_triangle(4,3,5),"Tam giac vuong")
	def test_vuong3(self):
		self.assertEqual(triangle.detect_triangle(4,5,3),"Tam giac vuong")
	def test_vuongcan1(self):
		self.assertEqual(triangle.detect_triangle(1,1,math.sqrt(2)),"Tam giac vuong can")
	def test_vuongcan2(self):
		self.assertEqual(triangle.detect_triangle(math.sqrt(2),1,1),"Tam giac vuong can")
	def test_vuongcan3(self):
		self.assertEqual(triangle.detect_triangle(1,math.sqrt(2),1),"Tam giac vuong can")
	def test_khongpaitamgiac1(self):
		self.assertEqual(triangle.detect_triangle(1,2,9),"Khong phai tam giac")
	def test_khongpaitamgiac2(self):
		self.assertEqual(triangle.detect_triangle(1,9,2),"Khong phai tam giac")
	def test_khongpaitamgiac2(self):
		self.assertEqual(triangle.detect_triangle(9,1,2),"Khong phai tam giac")
if __name__== '__main__':
	unittest.main()
	