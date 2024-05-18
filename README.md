# mass-shooter-classifier

In this project, we explored advanced fine-tuning methodologies for large language models (LLMs) to enhance their performance in identifying potential mass shooters from social media comments.

Instructions on running the code:

* Running the ensemble:

  In folder Ensemble_Model_Approach,

  Step 1:
  Run the following files on colab to train and test on specific trait models that form the ensemble:
  ensemble_mistral_manifesto.ipynb
  ensemble_supremacist_manifesto.ipynb
  ensemble_suicidal_manifesto.ipynb
  ensemble_terrorist_manifesto.ipynb

  Step 2:
  Download the generated label files from these codes.
  
  Step 3:
  Run the evaluate_ensemble.ipynb file to perform a majority vote and evaluate the model.

* Running the code for multistage fine tuning on Mistral:

  In folder Multistage_Fine_Tuning_Approach_Mistral,

  This folder contains codes to perform the multistage fine-tuning in various combinations of train and test sets.

  Step 1:
  Run the fine_tune_on_3_traits.ipynb to fine tune baseline Mistral sequentially on the three traits.

  Step 2:
  Run Train_manifesto_test_manifesto.ipynb to train the fine tuned model earlier and test on the main dataset.

  Step 3:
  Run the files TrainOn_traits_TestOn_manifestos_cross_val.ipynb and TrainOn_traits_TestOn_manifestos_n_pair.ipynb to train the models on traits and test them on the final dataset using two different loss functions.

* Running the code for multistage fine tuning on BERT:
    
  In folder Multistage_Fine_Tuning_Approach_BERT,
  
  Run the file Transformer_model_multistage_finetuning.ipynb
