#尾递归
#以前看lua有尾递归，现在python也有个尾递归

#函数的递归是基于栈实现的，每调用一个函数就会入一个栈，递归的层数过多则可能会造成栈溢出。

def tril(x):
	if(x<=1):
		return x;
	return x+tril(x-1); 
#像这样调用就栈溢出了。
#print(tril(1000))

#所以这里可以通过尾调用解决这个问题
#尾递归是指 在函数return的时候调用自身，但是不能有表达式，只是简单地调用自身，
#所以上面的调用不是尾递归
#解释器会对尾递归进行优化，每次进行尾递归的时候就会立马结束当前函数的栈的占用，进到下一个函数栈中，
#这样不管递归多少层，都只占一个栈，就不会溢出了。

def tril2(x,sum):
	if(x<=1):return sum;
	return tril2(x-1,sum+x);

#print(tril2(1000,0))
#坑了，廖雪峰的博客上，文章最后才说python没有尾递归。。。害我看开头的时候以为python也有尾递归。果然没有
