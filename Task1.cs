using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Input your string");
            var input = Console.ReadLine();
            Console.WriteLine("Input is : " + input);
            var words = input.Split(' ').Reverse();
            Console.WriteLine("Result is : " + string.Join(" ", words));
            Console.ReadKey();
        }
    }
}
