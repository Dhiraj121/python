#include<iostream>
using namespace std;
struct student
{
 char[10]Name;
 int Roll_no;
 float marks;
};

class student
{
 public:
 void accept();
 void display();
};

void student::accept()
{
 cout<<"Enter Student name";
 cout<<"Enter Roll_no";
 cout<<"Enter marks";
}

void Student::display()
{
 cin>>s.Name;
 cin>>s.Roll_no;
 cin>>s.marks;
}
void Student::display()
{
cout<<"Name"<<s.Naame;
cout<<"Roll_no"<<s.Roll_no;
cout<<"marks"<<s.marks;
}

student s2;
s2.accept();
s2.display();

};
