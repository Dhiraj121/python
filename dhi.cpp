#include<iostream>
using namespace std;

class student{

 public:	
	char name[30];
	int roll;
	int marks;
	
   void setData();
   void getData();
};

void student::setData(){
	cout<<"\nenter rollno  :";
	cin>>roll;
	cout<<"enter name :";
	cin>>name;
	cout<<"enter marks :";
	cin>>marks;
}

void student::getData(){
	
	cout<<roll<<"\t"<<name<<"\t"<<marks<<"\n";
	}

int main(){
	
	student stud[10];
	int i;
	cout<<"\nEnter student data :";
	
	for(i=0;i<2;i++){
		stud[i].setData();
	}

	cout<<"\ndisplay student data :\n";
		cout<<"roll\tname\tmarks\n";	
	for(i=0;i<2;i++){
		stud[i].getData();
	}
	
}
