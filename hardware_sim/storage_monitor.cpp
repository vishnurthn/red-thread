#include <iostream>
#include <vector>
#include <windows.h> // Specialized for Windows timing

using namespace std;

int main() {
    // Simulated temperature readings (in Celsius)
    vector<double> readings = {3.5, 4.0, 4.2, 5.8, 6.5, 7.2, 5.0};
    
    cout << "--- Smart Blood Storage System Active ---" << endl;
    cout << "Target Range: 2.0C - 6.0C" << endl;
    cout << "-----------------------------------------" << endl;

    for (double temp : readings) {
        cout << "Current Temperature: " << temp << "C | Status: ";
        
        if (temp > 6.0) {
            cout << "[CRITICAL] !!! TEMPERATURE EXCEEDED !!!" << endl;
            cout << ">> Action: Notifying Hospital Maintenance..." << endl;
        } else {
            cout << "[STABLE] Temperature within safe range." << endl;
        }

        // Wait for 1.5 seconds (1500 milliseconds)
        Sleep(1500); 
    }

    cout << "\nMonitoring Session Ended." << endl;
    return 0;
}