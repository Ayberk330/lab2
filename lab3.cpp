/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
using namespace std;
#include <iostream>
class Node{
    public:
    int data;
    Node *next;
    Node(int x,Node *n) {data = x;next =n;}
};
class Queue {
public:
    Node* front;  
    Node* rear;  
    int count;  


public:
    Queue() {
        front = rear = nullptr;
        count = 0;
    }
    

    void enqueue(int value) {
        Node* newNode = new Node(value,nullptr);
        if (rear == nullptr) {  
            front = rear = newNode;
        } else {
            rear->next = newNode; 
            rear = newNode;       
        }
        count++;
        std::cout << value << " added to queue"<<endl;
    }
    void dequeue() {
        if (isEmpty()) {
            std::cout << "queue is empty"<<endl;
            return;
        }
        Node* temp = front;  
        front = front->next;
        
        if (front == nullptr)
            rear = nullptr;

        delete temp;
    }
    int top(){
        if(isEmpty()){
            std::cout<<"queue is empty"<<endl;
            return -1;
            }
            return front ->data;
    }
    
    bool isEmpty(){
        return count==0;

        
    }
    void print(){
        for(Node* temp=front;temp !=nullptr;temp=temp->next){
        cout<<temp->data<<" ";
        
        }
    }
        
    
};
    int main()
{
    Queue q;
    q.enqueue(23);
    q.enqueue(12);
    q.enqueue(24);
    q.print();
    cout<<endl<<q.top()<<endl;
    
    
}
        
        
        
        
        
        
