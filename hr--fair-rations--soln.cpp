#include <iostream>
#include <vector>

using namespace std;

int soln(vector<int> b) {
	vector<int> odds;
	for (int i=0; i<b.size(); i++) {
		if (b[i]%2 != 0) {
			odds.push_back(i);
		}
	}
	if (odds.size()%2 != 0) {
		return -1;
	}
	int swaps = 0;
	for (int i=1; i<odds.size(); i +=2) {
		swaps += odds[i] - odds[i-1];
	}
	return 2*swaps;
}

int main() {
	int n;
	cin >> n;
	vector<int> b(n);
	for (int i=0; i<n; i++) {
		cin >> b[i];
	}
	int s = soln(b);
	if (s == -1) {
		cout << "NO" << endl;
	}
	else {
		cout << s << endl;
	}
	return 0;
}
