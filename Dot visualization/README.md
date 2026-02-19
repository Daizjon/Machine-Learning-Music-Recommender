# Decision Tree Visualization

This folder contains the exported `.dot` file of the trained Decision Tree model.

The file was generated to visualize the structure of the model and understand
how classification decisions are made based on age and gender inputs.

## Files

- `music-recommender.dot` – Graphviz representation of the trained decision tree

## Notes

To render the `.dot` file:

1. Install Graphviz
2. Run:

   dot -Tpng music-recommender.dot -o tree.png

This produces a visual diagram of the trained decision tree.

