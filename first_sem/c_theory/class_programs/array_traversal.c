#include<stdio.h>

int main(){
    int isValid=1;
    //calling method & stores returned value   
    //passing 'arraysizze'; int array_size=array
    while (isValid == 0)
    {
            int arraySize=read_array_size();
            int validated=validate_array_size(arraySize);
            if(validated == 1){
                
                break;

        }    
        printf("pls try again");

    }
}    
//read array SIZE from kb  
int read_array_size(){
    int size;   //local variable
    printf("Enter the array size[<4]:");
    scanf("%d",&size);
    return size;
}

int validate_array_size(int array_size){
    if(array_size >4)
}