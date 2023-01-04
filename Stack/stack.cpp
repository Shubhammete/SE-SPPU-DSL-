#include<bits/stdc++.h>
using namespace std;

class expression{
    public:
    string exp;
    int top,n;
    char arr[100];

    expression(){
        top = -1;
    }

    void input(){
        cout<<"Enter the String"<<endl;
        cin>>exp;
    }

    void push(){
        n = exp.length();
        for(int i = 0; i < n; i++){
            if(exp[i]== '(' or exp[i] =='{' or exp[i]== '['){
                top = top + 1;
                exp[i] = arr[top];
            }
        }
        if(top == -1){
            cout<<"Stack is empty!!!";
        }
        
    }
    void pop(){
        for(int i = 0; i < n; i++ ){
           if (exp[i] == ')' ||exp[i] ==']' || exp[i] == '}'){
              top --;
           }
        }
        if (top == -1){
            cout<<"Expression is correct";
        }
        else{
            cout<<"Expression is not correct";
        }
    }
};
int main()
{
    expression e;
    e.input();
    e.push();
    e.pop();
return 0;
}