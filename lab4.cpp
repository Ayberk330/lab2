/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }
    void push(int x) {
         if (num + 1 >= capacity) {
            increaseCapacity();
        }
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        num++;
    }

     int pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        Node* temp = head;
        int poppedValue = temp->data;
        head = head->next;
        delete temp;
        num--;
        return poppedValue;
    }
    int peek() {
    if(isEmpty()){
        cout<<"stack is empty"<<endl;
        
    }
    return head->data ;
        
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity *= 2;
        cout<<"capacity increased"<<endl;
    }

    bool deleteElement(int val) {
     if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return false;
        }
        Node* temp = head;
        Node* prev = nullptr;
        while (temp != nullptr && temp->data != val) {
            prev = temp;
            temp = temp->next;
        }

        if (temp == nullptr) {
            cout << "element not in stack." << endl;
            return false;
        }

        if (prev == nullptr) {
            head = temp->next;
        } else {
            prev->next = temp->next;
        }

        delete temp;
        num--;
        return true;
    
    }
     void printMystack() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << "  ";
            temp = temp->next;
            cout<<endl;
        }
        
    
    }
    
};

int main() {
    Stack myStack(2);
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);
    myStack.printMystack();
    myStack.push(23);
    myStack.push(24);
    myStack.push(21);
    
    myStack.pop();
    myStack.peek();
    myStack.deleteElement(10);
    myStack.push(99);
    myStack.printMystack();

    return 0;
}
