def tamgiac(a,b,c):
	if ( ( a+b > c ) & ( a+c > b ) & ( b+c > a ) ):
		if( ( a==b ) & ( b==c ) & (a==c) ):
			print " Tam giac deu "
			return
		if( (( a==b ) | ( a==c ) | ( b==c)) & ((a**2+b**2==c**2) | (a**2+c**2==b**2 ) | (b**2+c**2==a**2)) ):
			print " Tam giac vuong can"
			return
		if((a==b ) | ( a==c ) | ( b==c)):
			print " Tam giac can "
			return
		if((a**2+b**2==c**2) | (a**2+c**2==b**2 ) | (b**2+c**2==a**2)) :
			print " Tam giac vuong "
			return
		print " Tam giac thuong "
		return
	else :
		print " Khong phai tam giac "
