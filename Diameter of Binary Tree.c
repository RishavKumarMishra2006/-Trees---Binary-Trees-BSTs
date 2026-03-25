int diameterUtil(struct Node* root, int* height) {
    if (root == NULL) {
        *height = 0;
        return 0;
    }

    int lh = 0, rh = 0;

    int ld = diameterUtil(root->left, &lh);
    int rd = diameterUtil(root->right, &rh);

    *height = (lh > rh ? lh : rh) + 1;

    int curr = lh + rh + 1;

    return (curr > ld && curr > rd) ? curr : (ld > rd ? ld : rd);
}

int diameter(struct Node* root) {
    int height = 0;
    return diameterUtil(root, &height);
}
