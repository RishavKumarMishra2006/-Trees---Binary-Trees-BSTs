struct Node* mirror(struct Node* root) {
    if (root == NULL) return NULL;

    struct Node* temp = root->left;
    root->left = mirror(root->right);
    root->right = mirror(temp);

    return root;
}
