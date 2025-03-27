#include <iostream>
using namespace std;


double result = 0.0;


void recfunc(int n) {
    if(n == 0) {
        cout << "The harmonic sum is: " << result << endl;
        return;
    }
    result += 1.0 / n;
    recfunc(n - 1);
}


void recfunc() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    result = 0.0;
    recfunc(n);
}

int main() {
    recfunc();
    return 0;
}
