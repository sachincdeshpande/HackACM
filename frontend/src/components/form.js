import React, {Component} from 'react';

import { DropDownList } from '@progress/kendo-react-dropdowns';


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
            <div className ='Drop'>
            <DropDownList
                data={this.prof}
                textField= 'Name'
                dataItemKey="Summary"
                value={this.state.value}
                onChange={this.handleChange}
            />
            </div>

            <div className="example-config">
                {JSON.stringify(this.state.value.Summary)}
            </div>
        </div>
    );
}
}

export default NameForm;