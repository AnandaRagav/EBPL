# Simulated AI model for defect prediction
class MockModel:
def predict(self, image_input):
# Simulate prediction (0 = no defect, 1 = defect) with confidence
return 0.95 if image_input == "defective_image" else 0.05
# Simulated chatbot response function

def get_chatbot_response(user_query): 
	if "defect" in user_query.lower(): 
		return "The inspection system detected a defect with high confidence. Please review the item." 
	else: 
		return "I'm here to assist you with inspection-related queries."
# Simulated defect detection function (model passed as a parameter) def detect_defect(image, model): 
	prediction = model.predict(image) 
	return prediction > 0.9 # Threshold for detecting a defect
# Simulated alert trigger 
def trigger_alert(): 
	print("ALERT: Defect detected! Quality team notified.")
# Main program execution 
if __name__ == "__main__": 
	# Initialize mock model 
	model = MockModel()
# Example image input 
image_input = "defective_image" # Try "normal_image" to test non-defect
# Step 1: Run model prediction 
prediction = model.predict(image_input)


print(f"Prediction confidence: {prediction * 100:.2f}%")
# Step 2: Chatbot interaction 
user_query = "What is the defect status?" 
chatbot_response = get_chatbot_response(user_query) print("Chatbot:", chatbot_response)
# Step 3: Trigger alert if defect detected 
if detect_defect(image_input, model): 
	trigger_alert() 
else: 
	print("Item passed inspection. No defects found.")
