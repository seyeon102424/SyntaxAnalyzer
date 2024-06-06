#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class SLRTable {
private:
	vector<map<string, string>> table;
	vector<string> terminals;

public:
	SLRTable() {

        table.push_back({ {"vtype", "s2"}, {"VDECL", "1"} });
        table.push_back({ {"vtype", "s5"}, {"$", "r2"}, {"CODE", "3"}, {"VDECL", "1"}, {"FDECL", "4"} });
        table.push_back({ {"id", "s6"}, {"ASSIGN", "7"} });
        table.push_back({ {"$", "acc"} });
        table.push_back({ {"vtype", "s5"}, {"$", "r2"}, {"CODE", "8"}, {"VDECL", "1"}, {"FDECL", "4"} });
        table.push_back({ {"id", "s9"}, {"ASSIGN", "7"} });
        table.push_back({ {"semi", "s10"}, {"assign", "s11"} });
        table.push_back({ {"semi", "s12"} });
        table.push_back({ {"$", "r1"} });
        table.push_back({ {"semi", "s10"}, {"assign", "s11"}, {"lparen", "s13"} });
        table.push_back({{"vtype", "r3"}, {"id", "r3"}, {"rbrace", "r3"}, {"if", "r3"}, {"while", "r3"}, {"return", "r3"}, {"$", "r3"}});
        table.push_back({{"id", "s22"}, {"literal", "s16"}, {"character", "s17"}, {"boolstr", "s18"}, {"lparen", "s21"}, {"num", "s23"},{"RHS", "14"}, {"EXPR", "15"}, {"TERM", "19"}, {"FACTOR", "20"}});
        table.push_back({{"vtype", "r4"}, {"id", "r4"}, {"rbrace", "r4"}, {"if", "r4"}, {"while", "r4"}, {"return", "r4"}, {"$", "r4"}});
        table.push_back({{"vtype", "s25"}, {"rparen", "r19"}, {"ARG", "24"}});
        table.push_back({{"semi", "r5"}});
        table.push_back({{"semi", "r6"}});
        table.push_back({{"semi", "r7"}});
        table.push_back({{"semi", "r8"}});
        table.push_back({{"semi", "r9"}});
        table.push_back({{"semi", "r11"}, {"addsub", "s26"}, {"rparen", "r11"}});
        table.push_back({{"semi", "r13"}, {"addsub", "r13"}, {"multdiv", "s27"}, {"rparen", "r13"}});
        table.push_back({{"id", "s22"}, {"lparen", "s21"}, {"num", "s23"}, {"EXPR", "28"}, {"TERM", "19"}, {"FACTOR", "20"}});
        table.push_back({{"semi", "r15"}, {"addsub", "r15"}, {"multdiv", "r15"}, {"rparen", "r15"}});
        table.push_back({{"semi", "r16"}, {"addsub", "r16"}, {"multdiv", "r16"}, {"rparen", "r16"}});
        table.push_back({{"rparen", "s29"}});
        table.push_back({{"id", "s30"}});
        table.push_back({{"id", "s22"}, {"lparen", "s21"}, {"num", "s23"}, {"EXPR", "31"}, {"TERM", "19"}, {"FACTOR", "20"}});
        table.push_back({{"id", "s22"}, {"lparen", "s21"}, {"num", "s23"}, {"TERM", "32"}, {"FACTOR", "20"}});
        table.push_back({{"rparen", "s33"}});
        table.push_back({{"lbrace", "s34"}});
        table.push_back({{"rparen", "r21"}, {"comma", "s36"}, {"MOREARGS", "35"}});
        table.push_back({{"semi", "r10"}, {"rparen", "r10"}});
        table.push_back({{"semi", "r12"}, {"addsub", "r12"}, {"rparen", "r12"}});
        table.push_back({{"semi", "r14"}, {"addsub", "r14"}, {"multdiv", "r14"}, {"rparen", "r14"}});
        table.push_back({{"vtype", "s2"}, {"id", "s43"}, {"rbrace", "r23"}, {"if", "s44"}, {"while", "s45"}, {"return", "r23"}, {"VDECL", "39"}, {"ASSIGN", "40"}, {"BLOCK", "37"}, {"STMT", "38"}, {"MATCHED", "41"}, {"UNMATCHED", "42"}});
        table.push_back({{"rparen", "r18"}});
        table.push_back({{"vtype", "s46"}});
        table.push_back({{"return", "s48"}, {"RETURN", "47"}});
        table.push_back({{"vtype", "s2"}, {"id", "s43"}, {"rbrace", "r23"}, {"if", "s44"}, {"while", "s45"}, {"return", "r23"},{"VDECL", "39"}, {"ASSIGN", "40"}, {"BLOCK", "49"}, {"STMT", "38"}, {"MATCHED", "41"}, {"UNMATCHED", "42"}});
        table.push_back({{"vtype", "r24"}, {"id", "r24"}, {"rbrace", "r24"}, {"if", "r24"}, {"while", "r24"}, {"return", "r24"}});
        table.push_back({{"semi", "s50"}});
        table.push_back({{"vtype", "r26"}, {"id", "r26"}, {"rbrace", "r26"}, {"if", "r26"}, {"while", "r26"}, {"return", "r26"}});
        table.push_back({{"vtype", "r27"}, {"id", "r27"}, {"rbrace", "r27"}, {"if", "r27"}, {"while", "r27"}, {"return", "r27"}});
        table.push_back({{"assign", "s11"}});
        table.push_back({{"lparen", "s51"}});
        table.push_back({{"lparen", "s52"}});
        table.push_back({{"id", "s53"}});
        table.push_back({{"rbrace", "s54"}});
        table.push_back({{"id", "s22"}, {"literal", "s16"}, {"character", "s17"}, {"boolstr", "s18"}, {"lparen", "s21"}, {"num", "s23"},{"RHS", "55"}, {"EXPR", "15"}, {"TERM", "19"}, {"FACTOR", "20"}});
        table.push_back({{"rbrace", "r22"}, {"return", "r22"}});
        table.push_back({{"vtype", "r25"}, {"id", "r25"}, {"rbrace", "r25"}, {"if", "r25"}, {"while", "r25"}, {"return", "r25"}});
        table.push_back({{"boolstr", "s58"}, {"COND", "56"}, {"SIMPLECOND", "57"}});
        table.push_back({{"boolstr", "s58"}, {"COND", "59"}, {"SIMPLECOND", "57"}});
        table.push_back({{"rparen", "r21"}, {"comma", "s36"}, {"MOREARGS", "60"}});
        table.push_back({{"vtype", "r17"}, {"$", "r17"}});
        table.push_back({{"semi", "s61"}});
        table.push_back({{"rparen", "s62"}, {"comp", "s63"}});
        table.push_back({{"rparen", "r33"}, {"comp", "r33"}});
        table.push_back({{"rparen", "r34"}, {"comp", "r34"}});
        table.push_back({{"rparen", "s64"}, {"comp", "s63"}});
        table.push_back({{"rparen", "r20"}});
        table.push_back({{"rbrace", "r35"}});
        table.push_back({{"lbrace", "s65"}});
        table.push_back({{"boolstr", "s58"}, {"SIMPLECOND", "66"}});
        table.push_back({{"lbrace", "s67"}});
        table.push_back({{"vtype", "s2"}, {"id", "s43"}, {"rbrace", "r23"}, {"if", "s44"}, {"while", "s45"}, {"return", "r23"},{"VDECL", "39"}, {"ASSIGN", "40"}, {"BLOCK", "68"}, {"STMT", "38"},{"MATCHED", "41"}, {"UNMATCHED", "42"}});
        table.push_back({{"rparen", "r32"}, {"comp", "r32"}});
        table.push_back({{"vtype", "s2"}, {"id", "s43"}, {"rbrace", "r23"}, {"if", "s44"}, {"while", "s45"}, {"return", "r23"},{"VDECL", "39"}, {"ASSIGN", "40"}, {"BLOCK", "69"}, {"STMT", "38"},{"MATCHED", "41"}, {"UNMATCHED", "42"}});
        table.push_back({{"rbrace", "s70"}});
        table.push_back({{"rbrace", "s71"}});
        table.push_back({{"vtype", "r30"}, {"id", "r30"}, {"rbrace", "r30"}, {"if", "r30"}, {"else", "s72"}, {"while", "r30"}, {"return", "r30"}});
        table.push_back({{"vtype", "r29"}, {"id", "r29"}, {"rbrace", "r29"}, {"if", "r29"}, {"while", "r29"}, {"return", "r29"}});
        table.push_back({{"lbrace", "s73"}, {"if", "s75"}, {"UNMATCHED", "74"}});
        table.push_back({{"vtype", "s2"}, {"id", "s43"}, {"rbrace", "r23"}, {"if", "s44"}, {"while", "s45"}, {"return", "r23"},{"VDECL", "39"}, {"ASSIGN", "40"}, {"BLOCK", "76"}, {"STMT", "38"},{"MATCHED", "41"}, {"UNMATCHED", "42"}});
        table.push_back({{"vtype", "r31"}, {"id", "r31"}, {"rbrace", "r31"}, {"if", "r31"}, {"while", "r31"}, {"return", "r31"}});
        table.push_back({{"lparen", "s77"}});
        table.push_back({{"rbrace", "s78"}});
        table.push_back({{"boolstr", "s58"}, {"COND", "79"}, {"SIMPLECOND", "57"}});
        table.push_back({{"vtype", "r28"}, {"id", "r28"}, {"rbrace", "r28"}, {"if", "r28"}, {"while", "r28"}, {"return", "r28"}});
        table.push_back({{"rparen", "s80"}, {"comp", "s63"}});
        table.push_back({{"lbrace", "s81"}});
        table.push_back({{"vtype", "s2"}, {"id", "s43"}, {"rbrace", "r23"}, {"if", "s44"}, {"while", "s45"}, {"return", "r23"},{"VDECL", "39"}, {"ASSIGN", "40"}, {"BLOCK", "82"}, {"STMT", "38"},{"MATCHED", "41"}, {"UNMATCHED", "42"}});
        table.push_back({{"rbrace", "s83"}});
        table.push_back({{"vtype", "r30"}, {"id", "r30"}, {"rbrace", "r30"}, {"if", "r30"}, {"else", "s84"}, {"while", "r30"}, {"return", "r30"}});
        table.push_back({{"if", "s75"}, {"UNMATCHED", "74"}});

        terminals = {"vtype", "num", "character", "boolstr", "literal", "id", "if", "else", "while", "return", "addsub", "multdiv", "assign", "comp", "semi", "comma", "lparen", "rparen", "lbrace", "rbrace"};
	}

    string get_action(int cur_state, string input) {
        if (table[cur_state].find(input) != table[cur_state].end()) {
            return table[cur_state][input];
        }
        else { return "error"; }
    }
};