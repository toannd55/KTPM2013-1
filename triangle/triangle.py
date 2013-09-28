def detect_triangle(a,b,c):
	if( ( type(a) not in( int,float,long) ) | ( type(b) not in( int,float,long) ) | ( type(c) not in( int,float,long) ) ):
		return "Nhap khong dung kieu"
		
	if( (a<0) | (a>(2**32-1)) | (b<0) | (b>(2**32-1)) | (c<0) | (c>(2**32-1)) ):
		 return "So nhap vao khong dung"
	else:
		if ( ( a+b > c ) & ( a+c > b ) & ( b+c > a ) ):
			if( ( a==b ) & ( b==c ) & (a==c) ):
				return "Tam giac deu"
			if( (( a==b ) | ( a==c ) | ( b==c)) & ((round(a**2)+round(b**2)==round(c**2)) | (round(a**2)+round(c**2)==round(b**2) ) | (round(b**2)+round(c**2)==round(a**2))) ):
				return "Tam giac vuong can"
			if((a==b ) | ( a==c ) | ( b==c)):
				return "Tam giac can"
			if((round(a**2)+round(b**2)==round(c**2)) | (round(a**2)+round(c**2)==round(b**2) ) | (round(b**2)+round(c**2)==round(a**2))) :
				return "Tam giac vuong"
			return "Tam giac thuong"
		else :
			return "Khong phai tam giac"
