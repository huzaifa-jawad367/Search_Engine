// Search_engine_Datastructures.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std; 

class HashTables {

};

struct Lexicon {
    vector<string> words;
    HashTables pointers;
};

struct Hits {
    bool Capitalized; // checks for capitalization
    bool fancy; // due to absence of meta tags, anchor texts and stuff like that fancy text only checks for if the word is a title or not
    int position;
    int font_size;
};



int wordHashing(string wrd) {
    return wrd[1] + wrd[0] - (2 * 97);
}

struct avl {
    Hits node;
    struct avl* l;
    struct avl* r;
}*r;
class avl_tree {
public:
    int height(avl*);
    int difference(avl*);
    avl* rr_rotat(avl*);
    avl* ll_rotat(avl*);
    avl* lr_rotat(avl*);
    avl* rl_rotat(avl*);
    avl* balance(avl*);
    avl* insert(avl*, int);
    void show(avl*, int);
    void inorder(avl*);
    void preorder(avl*);
    void postorder(avl*);
    avl_tree() {
        r = NULL;
    }
};
int avl_tree::height(avl* t) {
    int h = 0;
    if (t != NULL) {
        int l_height = height(t->l);
        int r_height = height(t->r);
        int max_height = max(l_height, r_height);
        h = max_height + 1;
    }
    return h;
}
int avl_tree::difference(avl* t) {
    int l_height = height(t->l);
    int r_height = height(t->r);
    int b_factor = l_height - r_height;
    return b_factor;
}
avl* avl_tree::rr_rotat(avl* parent) {
    avl* t;
    t = parent->r;
    parent->r = t->l;
    t->l = parent;
    cout << "Right-Right Rotation";
    return t;
}
avl* avl_tree::ll_rotat(avl* parent) {
    avl* t;
    t = parent->l;
    parent->l = t->r;
    t->r = parent;
    cout << "Left-Left Rotation";
    return t;
}
avl* avl_tree::lr_rotat(avl* parent) {
    avl* t;
    t = parent->l;
    parent->l = rr_rotat(t);
    cout << "Left-Right Rotation";
    return ll_rotat(parent);
}
avl* avl_tree::rl_rotat(avl* parent) {
    avl* t;
    t = parent->r;
    parent->r = ll_rotat(t);
    cout << "Right-Left Rotation";
    return rr_rotat(parent);
}
avl* avl_tree::balance(avl* t) {
    int bal_factor = difference(t);
    if (bal_factor > 1) {
        if (difference(t->l) > 0)
            t = ll_rotat(t);
        else
            t = lr_rotat(t);
    }
    else if (bal_factor < -1) {
        if (difference(t->r) > 0)
            t = rl_rotat(t);
        else
            t = rr_rotat(t);
    }
    return t;
}
avl* avl_tree::insert(avl* r, int v) {
    if (r == NULL) {
        r = new avl;
        r->d = v;
        r->l = NULL;
        r->r = NULL;
        return r;
    }
    else if (v < r->d) {
        r->l = insert(r->l, v);
        r = balance(r);
    }
    else if (v >= r->d) {
        r->r = insert(r->r, v);
        r = balance(r);
    } return r;
}
void avl_tree::show(avl* p, int l) {
    int i;
    if (p != NULL) {
        show(p->r, l + 1);
        cout << " ";
        if (p == r)
            cout << "Root -> ";
        for (i = 0; i < l && p != r; i++)
            cout << " ";
        cout << p->d;
        show(p->l, l + 1);
    }
}
void avl_tree::inorder(avl* t) {
    if (t == NULL)
        return;
    inorder(t->l);
    cout << t->d << " ";
    inorder(t->r);
}
void avl_tree::preorder(avl* t) {
    if (t == NULL)
        return;
    cout << t->d << " ";
    preorder(t->l);
    preorder(t->r);
}
void avl_tree::postorder(avl* t) {
    if (t == NULL)
        return;
    postorder(t->l);
    postorder(t->r);
    cout << t->d << " ";
}

class Barrel {
    

};



int main() {
    
}