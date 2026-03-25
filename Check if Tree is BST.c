int isBSTUtil(struct Node* root, int min, int max) {
    if (root == NULL) return 1;

    if (root->data <= min || root->data >= max)
        return 0;

    return isBSTUtil(root->left, min, root->data) &&
           isBSTUtil(root->right, root->data, max);
}

int isBST(struct Node* root) {
    return isBSTUtil(root, -100000, 100000);
}
