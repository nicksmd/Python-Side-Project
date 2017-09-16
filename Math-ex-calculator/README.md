# Math expression calculation

##Problem:
__Input:__ An math expression includes operands: real numbers; operators: plus(+), minus(-), multiply(*), devide(/) and brackets ()

__Output:__ Value of the given expression

__Example:__
~~~
Input: (-2+(2-3)*4)/2
Output: -3
~~~

##Algorithm:

1. Pre-process
	- Replace continuous pluses and minuses by single plus or minus by counting the number of minuses:
	  if the number of minuses is odd then replace by one minus 
	  else replace  by one plus.
	- Handle negative operands by adding one zero before any plus or minus with no operand before it.
	For example: -7+6 = 0-7+6
	- Split the input string into an array of operands, brackets and operators
	- Convert infix order to postfix order by stack
	
		For example:
	
		Q=a*(b+c)-d/5 => P=a b c + * d 5 / -
	
		__Pseudo code__
		~~~
		Stack.Clear;
		For (T = elements of INFIX){
			Switch (T) {
				Case ‘(’: Stack.Push(T);
				Case ‘)’: Do {
						X = Stack.Pop;
						If (X <> ’(‘) Print(X);
					   }While(X != ’(‘);			
				Case +, -, *, /: {
		While (!Stack.Empty && Priority(T) <= Priority(Stack.Top)) Print(Stack.Pop);
		Stack.Push(T);
		}
				Default: Print(T);
			}
		}
		While (!Stack.Empty) Print(Stack.Pop);
		~~~
		Priority of operator
		


		|    |      |
		|:---|:-----|
		|(   |0     | 
		|+,- |1     |
		|*,/ |2     |

2. Process

	Scan the Postfix stack from left to right.
	- Initialise an empty stack.
	- If the scannned element is an operand, push it to the stack. 
	  If the scanned element is an operator, then we calculate the 2 top most elements of the stack (simultaneously, pop them from stack) then push the result to stack.
	- Repeat this step till all the elements are scanned.
	- After all elements are scanned, we will have only one element in the stack. It is the result of our problem. Return top of stack.
