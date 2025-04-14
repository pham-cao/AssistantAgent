from crew import crew

student_question = "Em muốn biết học phí ngành Kỹ thuật phần mềm năm nay là bao nhiêu?"

result = crew.kickoff(inputs={
    "question": student_question,
    "requirement_type": "học phí ngành Kỹ thuật phần mềm",  # gán tạm, thật ra agent sẽ tạo ra cái này
    "retrieved_info": "Học phí KTPM năm 2024 là 1.200.000 VNĐ/tín chỉ. Tổng trung bình 45 triệu/năm."
})

print(result)
