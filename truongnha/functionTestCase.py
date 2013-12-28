#Tinh diem trung binh
#Xet hoc luc
#Xet danh hieu
#Dua tren thong tin cua trang web http://thuvienphapluat.vn/archive/Thong-tu/Thong-tu-58-2011-TT-BGDDT-Quy-che-danh-gia-xep-loai-hoc-sinh-trung-hoc-co-so-vb133268t23.aspx

import math

#Ham Tinh Diem Trung Binh Cua Mot Hoc Sinh Tu Day Diem Thanh Phan
def Diem_Trung_Binh(array1 = [], array2 = []):
	sum = 0.00
	count = 0.00
	
	for element1 in array1:
		sum = sum + float(element1)
		count = count + 1
	for element2 in array2:
		sum = sum + float(element2)
		count = count + 1
	if count > 0 :
		avg = sum/count
		return round(avg, 1)
	else:
		return 0

#Ham tra ve tong 2 gia tri
def add(value1, value2):
	number = int(value1) + int(value2)
	return number
		
#Them gia tri vao mot danh sach
def append_to_lists(list, *values):
	for element in values:
		list.append(element)

#So sanh list diem voi mot gia tri nao do tra ve True(1) hoac False(0)
def	So_Sanh(value, array=[]):
	for element in array:
		if float(element) < float(value):
			return 0
	return 1
	
#Ham tra ve hoc luc cua hoc sinh
def Tinh_Hoc_Luc(diemTheDuc, diemTB, array1=[], array2=[]):
	'''
		1. Loại giỏi, nếu có đủ các tiêu chuẩn sau đây:
			a) Điểm trung bình các môn học từ 8,0 trở lên, trong đó điểm trung bình của 1 trong 2 môn Toán, Ngữ văn từ 8,0 trở lên;
			riêng đối với học sinh lớp chuyên của trường THPT chuyên phải thêm điều kiện điểm trung bình môn chuyên từ 8,0 trở lên;
			b) Không có môn học nào điểm trung bình dưới 6,5;
			c) Các môn học đánh giá bằng nhận xét đạt loại Đ.
		2. Loại khá, nếu có đủ các tiêu chuẩn sau đây:
			a) Điểm trung bình các môn học từ 6,5 trở lên, trong đó điểm trung bình của 1 trong 2 môn Toán, Ngữ văn từ 6,5 trở lên;
			riêng đối với học sinh lớp chuyên của trường THPT chuyên phải thêm điều kiện điểm trung bình môn chuyên từ 6,5 trở lên;
			b) Không có môn học nào điểm trung bình dưới 5,0;
			c) Các môn học đánh giá bằng nhận xét đạt loại Đ.
		3. Loại trung bình, nếu có đủ các tiêu chuẩn sau đây:
			a) Điểm trung bình các môn học từ 5,0 trở lên, trong đó điểm trung bình của 1 trong 2 môn Toán, Ngữ văn từ 5,0 trở lên;
			riêng đối với học sinh lớp chuyên của trường THPT chuyên phải thêm điều kiện điểm trung bình môn chuyên từ 5,0 trở lên;
			b) Không có môn học nào điểm trung bình dưới 3,5;
			c) Các môn học đánh giá bằng nhận xét đạt loại Đ.
		4. Loại yếu: Điểm trung bình các môn học từ 3,5 trở lên, không có môn học nào điểm trung bình dưới 2,0.
		5. Loại kém: Các trường hợp còn lại.
	'''

	diemToan = float(array1[0])
	diemVan = float(array1[5])
	diemTrungBinh = float(diemTB)
	
	if diemTrungBinh >= 8.0:
		if (diemToan >= 8.0 or diemVan >= 8.0):
			if diemTheDuc == unicode("Đ", 'utf-8') and So_Sanh(6.5, array1) == 1 and So_Sanh(6.5, array2) == 1:
				return unicode("Giỏi", 'utf-8')
	if diemTrungBinh >= 6.5:
		if (diemToan >= 6.5 or diemVan >= 6.5):
			if diemTheDuc == unicode("Đ", 'utf-8') and So_Sanh(5.0, array1) == 1 and So_Sanh(5.0, array2) == 1:
				return unicode("Khá", 'utf-8')
	if diemTrungBinh >= 5.0:
		if (diemToan >= 5.0 or diemVan >= 5.0):
			if diemTheDuc == unicode("Đ", 'utf-8') and So_Sanh(3.5, array1) == 1 and So_Sanh(3.5, array2) == 1:
				return unicode("TB", 'utf-8')
	if diemTrungBinh >= 3.5:
		if So_Sanh(array1, 2.0) == 1 and So_Sanh(array2, 2.0) == 1:
			return unicode("Yếu", 'utf-8')
	return unicode("Kém", 'utf-8')
	
def Tinh_Danh_Hieu(hocLuc, hanhKiem):
	'''
		1. Công nhận đạt danh hiệu học sinh giỏi học kỳ hoặc cả năm học, nếu đạt hạnh kiểm loại tốt và học lực loại giỏi.
		2. Công nhận đạt danh hiệu học sinh tiên tiến học kỳ hoặc cả năm học, nếu đạt hạnh kiểm từ loại khá trở lên và học lực từ loại khá trở lên. 
	'''
	
	if hocLuc == unicode("Giỏi", 'utf-8'):
		if hanhKiem == unicode("T", 'tf-8'):
			return unicode("HSG", 'utf-8')
		elif hanhKiem == unicode("K", 'tf-8'):
			return unicode("HSTT", 'utf-8')
	if hocLuc == unicode("Khá", 'utf-8'):
		if hanhKiem == unicode("T", 'utf-8') or hanhKiem == unicode("K", 'utf-8'):
			return unicode("HSTT", 'utf-8')
	return ""