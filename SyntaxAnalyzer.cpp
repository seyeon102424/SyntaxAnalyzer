#include <iostream>
#include <string>
#include <deque>
#include <sstream>
#include "SLRTable.cpp"

using namespace std;

class SyntaxAnalyzer {
private:
	SLRTable* table;
	deque<int> stack;
	deque<string> right_sub;

public:
	SyntaxAnalyzer(SLRTable* table) : table(table) {
		stack.push_back(0);
	}
	void ActionTable();

	void verify(const string& line) {
		if (line.empty()) {
			cout << "The line is empty." << endl;
		}

		istringstream iss(line);
		string token;

		while (iss >> token) { right_sub.push_back(token); }
		right_sub.push_back("$");

		while (!right_sub.empty()) {
			int cur_state = stack.back();
			string next_input = right_sub.front();

			string action = table -> get_action(cur_state, next_input);
		}
	}

};

void SyntaxAnalyzer::ActionTable() {

}