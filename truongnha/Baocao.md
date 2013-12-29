KIỂM THỬ VÀ ĐẢM BẢO CHẤT LƯỢNG PHẦN MỀM 

Báo Cáo Bài Tập Lớn

I.	Giới thiệu
-	Thành viên	
o	Nguyễn Thanh Tuyền
o	Trần Văn Trinh
o	Nguyễn Đức Toàn
o	Nguyễn Thành Trung
o	Hoàng Kim Băng
-	Module tested
o	Lịch Học
o	Điểm Danh
o	Nhập Hạnh Kiểm
o	Tính Tổng Kết 
II.	Công Việc
1.	Hướng dẫn chạy
o	Ở ngoài thư mục cha của các thư mục test , ta mở command line và chạy dòng lệnh
pybot	[folder_name]
2.	Các lỗi phát hiện mà không test được
o	Lỗi khi nhập điểm từ file excel :
	Khi nhập điểm từ file excel , các ô điểm có chứa giá trị thập phân sẽ gây lỗi site ( Lớp 11B bị lỗi không vào lại được sau khi nhập điểm )
o	Lỗi thêm sinh viên từ file excel
	Khi nhập các sinh viên có tên và năm sinh giống nhau sẽ không được ghi nhận , mặc dù các lớp là khác nhau
 
o	 Lỗi khi nhập hạnh kiểm của 1 lớp
	Khi nhập hạnh kiểm của 1 lớp, lưu nó vào sang phần tính tổng kết, rồi sau đó ta quay lại xóa hết hạnh kiểm vừa nhập đi, quay lại phần tổng kết khi click vào "Tính trung bình và xét danh hiệu" thì nó vẫn báo là "đã đủ hạnh kiểm" mặc dù ô hạnh kiểm trống.
	Khi nhập hạnh kiểm , hạnh kiểm học kì 2 bị disable nhưng các tháng 1,2,3,4,5 vẫn có thể nhập hạnh kiểm

3.	 Chi tiết các chức năng đã test

STT	Tên	Mô tả	P/F
1	Login	Login vào hệ thống	Passed
2	Goto Class	Đi đến lớp muốn test	Passed
3	Goto Function	Đi đến chức năng muốn test	Passed
4	Điểm danh
(*)	4.1 Input to Cell	Nhập nhiều giá trị vào 1 ô	Passed
		4.2 Input to Column Date	Nhập nhiều giá trị vào 1 cột ( ngày 28/12/2013)	Passed
		4.3 Input to Column Date3	Nhập nhiều giá trị vào 1 cột ( ngày 23/12/2013)	Failed
5	Hạnh kiểm
(*)	5.1 Input to Cell	Nhập nhiều giá trị 1 ô	Passed
		5.2 Input to Cells	Nhập các giá trị ngẫu nhiên vào các cột ngẫu nhiêu	Passed
		5.3 Input to Row	Nhập nhiều giá trị vào từng ô của 1 dòng	Passed
6	Thời Khóa Biểu	6.1 Input to Cell	Nhập nhiều giá trị vào 1 ô	Passed
		6.2 Input Mutil Value To Column	Nhập nhiều giá giá vào 1 cột	Passed
		6.3 Input Mutil Value To Row	Nhập nhiều giá trị 1 dòng	Passed
7	Tính Tổng Kết	Tính tổng kết	Lấy các giá trị trong ô ,tính tổng kết so sánh với kết quả	Passed

Note :
o	Các test (*) passed khi các dữ liệu trống , nếu dữ liệu không trống có lúc 1 số test bị failed , nhưng run lại 1 lần nữa sẽ passed
o	Từ Test Hạnh kiểm : Tuy test 4.2 passed , khi test 4.3 failed thì phát hiện ID bị đánh lẫn lộn, không đúng thứ tự ( Hình ảnh minh họa trong thư mục Screenshot )

4.	Những khó khăn khi làm 

o	Tìm hiểu keyword
o	Tài liệu hướng dẫn ít
o	Nhiều bảng trong site không có ID

5.	Góp ý cho hệ thống
o	Phần tính điểm bọn e nghĩ chưa hợp lý vì có thể có trường chuyên , phân ban  thì cách tính điểm môn chuyên , môn phân ban sẽ được nhân đôi
o	Phần hạnh kiểm nếu kì học đang là kì 1 thì các tháng 1,2,3,4,5 nên bị disable 


