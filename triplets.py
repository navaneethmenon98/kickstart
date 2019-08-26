def nodig(x):
	t=0
	while(x>=1):
		x=x/10
		t=t+1
	return t

T=int(raw_input())
for f in range(T):
	count = 0
	N= int(raw_input())
	A= map(int,raw_input().split())
	z=0
	while (z<N):
		y=0
		while(y<z):
			x=0
			while(x<y):
				if(A[x]==A[y]*A[z] or A[y]==A[x]*A[z] or A[z]==A[x]*A[y]):
						
					count=count+1
					
				x=x+1
			y=y+1
		z=z+1
				
	print 'Case #%d: %d' %(f+1,count)
		
