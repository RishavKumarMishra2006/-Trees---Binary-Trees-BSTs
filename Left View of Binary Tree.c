void leftViewUtil(struct Node* root, int level, int* maxLevel) {
    if (root == NULL) return;

    if (*maxLevel < level) {
        printf("%d ", root->data);
        *maxLevel = level;
    }

    leftViewUtil(root->left, level + 1, maxLevel);
    leftViewUtil(root->right, level + 1, maxLevel);
}

void leftView(struct Node* root) {
    int maxLevel = 0;
    leftViewUtil(root, 1, &maxLevel);
}
