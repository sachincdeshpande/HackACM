import React, {Component} from 'react';
import {  DropDownList, ComboBox } from '@progress/kendo-react-dropdowns';
import { Dropdown } from 'react-bootstrap';




class NameForm extends Component {
  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(e) {
    alert('The value is: ' + this.input.value);
    e.preventDefault();
    
  }

  prof = [
    {
      Name: "Patrick Tantalo",
      Summary: "The grade was based on 7 labs (10% grade), 5 projects (20% grade), two mid terms (20% each), and a final( 30% grade). Most of his labs are straight forward and informative. A couple of his project assignments are difficult but he gives many due date extensions. Mid terms and final are similar to the review sheets so study them and u'll be chilling. Pretty clear professor, though a bit on the easy side. If you've taken one of his classes, you'll know exactly how they go. 2 midterms and a final, all of which draw heavily from the review problems/homework sets. Programming assignments are really, really easy. Took him for 12A, 12B, 101, got A's each time. Might take him for 201. Good professor. Tantalo is a great professor who gives lots of materials to get students started on the assignments. The assignments still aren't all easy, but he makes sure you understand how to do them and what they are. Also he almost always extends every assignment by a week. Straightforward exams and class. Great professor. Class was easier than I thought it would be. Tests are surprisingly easy. Programming assignments were interesting and not too difficult. Lecture sometimes is boring and irrelevant. Class didn't feel very coherent. Homework was difficult, and didn't really relate to tests. He's a decent lecturer. The TA's took a long time to return assignments."
    },
    {
      Name: "Darrell Long",
      Summary: "Darrell can come off mean, but he's one of the nicest, most caring and kind professors/people I've ever meet. He's widely known for his 12B class, but that's reasonable. The class was hard, but very rewarding IMO. Take a class with him, you'll come out w/ some valuable life lessons and lots of self discipline. Not the class you want, but need. The learning environment felt nonexistent. Professor refused to answer a question in class in the last week because he expected us to know it since the beginning of the quarter. Condescending to say the least. Not sure if even a quarter of the class passed. He threatened to not curve the class when someone asked about. Don't think there was one. Hardest class ever. Class moves way too fast. He doesn't want to answer questions he thinks you should already know like the back of your hand. He has extremely high expectations on you, but it's unclear on what he wants to see in your programs other than them working. You will do well if you reference outside sources from the class like textbook. He is very knowledgeable on the material, but he has really given the class such a hard time and for such an important class too. Assignments are very interesting, but it was hard to enjoy the class. Lab sections are useful but heavily packed making it nearly impossible to get the help you need. Take this class with a different professor."
    },
    {
      Name: "David Draper",
      Summary: "His voice is very monotone which made it hard not to fall asleep and his writing is very messy. The class was hard however the professor would help a lot during office hours and during midterm and finals he would extend his office hours. Also everything is open-book and the class is webcasted. Draper is the man! AMS 131 is a difficult course but he made it easier. There are three take home tests and gives quizzes at each section. He and his TA's provide office hours everyday of the week. GO TO THEM! THEY ARE EXTREMELY USEFUL FOR THE TAKE HOME TESTS!! He even had additional office hours during week 5 for the last test. He's hilarious too! Definitely take him for AMS 7 if you have the option. His final and midterm are both take home and you can ask any questions you have about the exams during office hours. He even has extra office hours  on the weekend during finals week. Section is mandatory and there's a small quiz at the end of each section. Make sure not to skip class. Draper really cares about his students. He is a great professor and a great human being! It is very easy to find help in his class when you need it. Lectures are very helpful if you want to get a good understanding of the class and he gives a take home midterm and final. I would recommend this class for anyone who needs stats."
    },
    {
      Name: "Yonatan Katznelson",
      Summary: "definitely one of the hardest classes I've taken, BUT, Katznelson is a fair grader. He gives you a perfect outline/ material that will be covered in midterms/final. Not mandatory to go to class, but he gives you quizzes either before or after his lecture. DONT take him if you're not willing to put in the work. I went to MSI, section & small group."
    },
    {
      Name: "Peter Alvaro",
      Summary: "I think he's just used to teaching higher level classes. first 3 week lectures were ok. Sections were hit or miss helpful (my TA had a lot of attitude so I had to switch sections). Homeworks and midterm were doable, but final average was an F. The class overall wasn't too bad, but not recommended for someone who wants to take an intro python class I like Peter, but not his class. He's a nice guy and you can tell he cares. the problem is he allows TAs to have absolute control over the grades, and have them create assignments TOO DIFFICULT for an intro class. If you make a mistake on even one line of code, it's an F. The final was extremely difficult. Would never take him again As a class, this was super easy. But that's because I like python and I read the textbook. The lectures are dense, boring and pointless. He treats the class as a chance to write code collaboratively, which really means writing some random code then troubleshooting it in front of the class for 20 min when he forgets w colon. The Hw was fun though. By far one of the best professors in the department. If you have the chance to take a class with him, do it. He's nice, caring, and easy to talk to, and his lectures are involved, entertaining, and interactive. The class is difficult and theoretically intense, and there is no course textbook so lecture attendance is very important."
    },
    {
      Name: "Seshadhri Commadur",
      Summary: "I've taken 12B and 101 with Sesh and had a good experience, so I chose to take 130 with him. What followed was by far the hardest class I've ever taken. Sesh does a pretty good job of teaching, but dear lord this is a beast of a class. It was his first time teaching it so it might be easier next time, but be aware that Sesh does not go easy here. Just listening to lecture and writing stuff down isn't going to cut it for this class. A lot of work outside of lecture and homework is required to succeed in this class. Luckily, Sesh does curve really well and his TA's are always available for outside help. One thing that will really help you out in this course is forming a study group. Sesh is by far the best professor I've ever had. His class is hard, brutally hard, especially if you're coming from CS11 but if you put the time in, you will learn an incredible amount. I easily spent 20+ hours a week on his class but it was well worth it Awesome professor. I learned A LOT from his class. His HWs were definitely very challenging. Although the HWs were hard, you learn a ton by doing them (and that's where most of your learning comes from). He's very generous with his grade curves, but you still have to work for your grade. Expect to spend tons of time outside class doing his HW."
    },
    {
      Name: "Allen Van Gelder",
      Summary: "Worst professor Ive ever had. Doesn't explain what he's teaching, expects you to know content not taught yet. Labs are very difficult with confusing instructions and little feedback. Asked him a question about my lab and he said, I don't care. Grades labs with a harsh script and refuses to look over code for regrade. Do not take his class. The assignments are not hard, but the main problem at this class is that the requirements for the programming assignment are very unclear. Thus, your program can work, but you will have 50% of grade. I think, a lot of students got the programs from their friends who took this class with this professor before and they fixed the mistakes. Van Gelder is probably one of the worst professors Ive had. Most of what I learned in his class was either taught to me by other students that had previously learned the material, or through the text book. He graded all of our programs via a script that didnt work and probably more than a third of the class got an incomplete, due to the script. I found the overall structure of the class conducive to learning the material, though his lectures could be more organized.  Programs complement current class topics and exams are fair. More than enough resources are extended for students to do well in this class, and AVG is attentive to student needsresponsive to questions if you reach out."
    },
    {
      Name: "Ethan Miller",
      Summary: "Worst professor at UCSC. Doesn't give the proper tools for students to succeed, makes it unnaturally hard for students to learn. He won't post solutions to homework because he's afraid someone will post it online or something. I have no doubt he's really smart, but his class is sometimes so insanely hard, very demoralizing for cs students imo. His lectures wouldn't be bad if he didn't get sidetracked by people making sarcastic or unnecessary comments during class. The material in the lectures and the readings supplement each other very well, and it's the best way of learning in my opinion. The homework is often confusing and takes far too long, and can sometimes be very tedious. omg, the cm110 class is so crazy under him, the most recent homework is absolutely unable to finish within the time he gave to us, plus, most of the materials used in homework is not fairly covered in his lecture. I spend over 20 hours to do his homework and still not finished . I think he expects too much from his student. He graded students on 9 extremely lengthy, overly-challenging assignments, and the midterm & final exams. Even though I worked harder than I ever have in any class, I received low grades throughout the quarter. He makes it impossible to learn, doesn't explain the material enough, and expects everyone to know how to code without working w/ anyone."
    },
    {
      Name: "Tracy Larrabee",
      Summary: "Most enjoyable lectures @ UCSC. One Quiz & HW every week. Class is easy if you keep up with the lecture, go to MSI, section and class (takes time). She's hilarious and very clear, loud and easy to follow. She cares about UCSC students and also works in the admin. Take every class you can with her. CE 16 regardless, is still challenging. I took this class about 1 year ago. She is funny and pretty good at what she does. The only reason I got an A- was because I didn't do so well on the final. You need to pass the final to pass the class. The material was not hard and when she teaches it, its an easy class. Wonderful teacher, prolly the best for CE! 40% quizzes and 50% final. Quizzes aren't hard nor easy, she tells you whats on it the day before and goes over the topics right before. STUDY for the final, hardest part of the class. Lots of partial credit. Make sure u go to MSI so u can get that 5% extra credit and extra help, they are extremely helpful She is alright. People love her cuz she's easy. However, she doesn't prepare you enough for upper-div classes. Go to class, she'll tell u what's gonna be on the quizzes and the final.  Final is 45% of your grade and it's harder than the quizzes so be ready. Class' TAs are great. She spend a lot of time talking random stuff than actually lecturing."
    },
    {
      Name: "Roger Anderson",
      Summary: "I felt that there was a great disconnect between the lectures, and things that were needed to do the homework and tests. His tests were very difficult, for example both midterms had a class averages in the 30's. They also were not similar to the practice tests. I learned everything from my TA, so it was fortunate that the class had good TA's. Professor Anderson is a nice guy, but not a good teacher.  I attended all his lectures, aced most problems in the book (including the assigned hw), and went to sections regularly.  I ended with a D in his class-- the first non-passing grade I've ever had. It's almost impossible to get the right answers on his exams, unless you're gifted. Anderson is a nice guy, but not a good teacher.  I attended all his lectures, aced most problems in the book, and went to sections regularly. Nevertheless, like everyone else is saying, his exams are impossible no matter how hard you try. I ended with a D in this class, but I knew I did my best. I mean, what else can I say... JUST DON'T TAKE HIS CLASS if you want to stay awake..he's not clear, he's not organized..you would fall asleep in class most of the time..he shows too much graphs he doesn't even specify...i did not enjoy learning chem because of his class."
    }
];
state = {
    // Since the reference of the initial value is not from the 'sports' collection,
    // 'dataItemKey' have to be set.
    value: { Name: 'Patrick Tantalo', Summary: "The grade was based on 7 labs (10% grade), 5 projects (20% grade), two mid terms (20% each), and a final( 30% grade). Most of his labs are straight forward and informative. A couple of his project assignments are difficult but he gives many due date extensions. Mid terms and final are similar to the review sheets so study them and u'll be chilling. Pretty clear professor, though a bit on the easy side. If you've taken one of his classes, you'll know exactly how they go. 2 midterms and a final, all of which draw heavily from the review problems/homework sets. Programming assignments are really, really easy. Took him for 12A, 12B, 101, got A's each time. Might take him for 201. Good professor. Tantalo is a great professor who gives lots of materials to get students started on the assignments. The assignments still aren't all easy, but he makes sure you understand how to do them and what they are. Also he almost always extends every assignment by a week. Straightforward exams and class. Great professor. Class was easier than I thought it would be. Tests are surprisingly easy. Programming assignments were interesting and not too difficult. Lecture sometimes is boring and irrelevant. Class didn't feel very coherent. Homework was difficult, and didn't really relate to tests. He's a decent lecturer. The TA's took a long time to return assignments." }
};

handleChange = (event) => {
    this.setState({
        value: event.target.value
    });
}


  render() {
    return (
        
        <div>
              <div class = 'row'>
               <div class = 'col-3 my-col' id='drop'> 
                  <div className ='Drop'>
                
                  <ComboBox
                      data={this.prof}
                      textField= 'Name'
                      dataItemKey="Summary"
                      value={this.state.value}
                      onChange={this.handleChange}
                  />

                  </div>
                </div>
                  <div class = 'col-9 my-col'>
                    <div className="example-config">
                        {JSON.stringify(this.state.value.Summary)}
                    </div>
                  </div>
                </div>
        </div>
    );
}
}

export default NameForm;