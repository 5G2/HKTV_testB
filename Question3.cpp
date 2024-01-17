#include <iostream>
#include <vector>

using namespace std;
void maxQuantity(int c_length,int c_width, int c_height, int p_length, int p_width, int p_height) {
    if(c_length<p_length||c_height<p_height||c_width<p_width){
        cout<<0;
        return;
    }
    int length_diff=c_length/p_length;
    int width_diff=c_width/p_width;
    int height_diff=c_height/p_height;

    int total=length_diff*width_diff*height_diff;
    cout<<total;
}

int main() {
   maxQuantity(320,260,200,210,35,35);
    return 0;
}
