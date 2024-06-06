#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "SLRTable.cpp"
#include "SyntaxAnalyzer.cpp"

using namespace std;

int main(int argc, char*argv[]) {

    if (argc < 2) {
        cerr << "Error : no input file" << endl;
        return 1;
    }

    std::string file_path = argv[1];
    std::ifstream input_file(file_path);
    std::string line;
    int line_num = 0;

    if (!input_file.is_open()) {
        cerr << "Failed to open file" << endl;
        return 1;
    }

    SLRTable slr_table;
    SyntaxAnalyzer syntaxalayzer(&slr_table);

    while (getline(input_file, line)) {
        line_num++;
    }

}